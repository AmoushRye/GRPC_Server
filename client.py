import grpc
import dog_pb2
import dog_pb2_grpc

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = dog_pb2_grpc.DogServiceStub(channel)
        id = int(input("Enter the id for the dog:"))
        # Create a request for a dog with ID
        dog_request = dog_pb2.DogRequest(id=id)
        response = stub.GetDog(dog_request)
        
        if response.dog.breed:
            print(f"ID: {response.dog.id}")
            print(f"Breed: {response.dog.breed}")
            print(f"Age Limit: {response.dog.age_limit} years")
            print(f"Description: {response.dog.description}")
        else:
            print("Dog ID not found")

if __name__ == '__main__':
    run()
