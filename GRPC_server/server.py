import grpc
from concurrent import futures
import GRPC_server.dog_pb2 as dog_pb2
import GRPC_server.dog_pb2_grpc as dog_pb2_grpc

# Sample data store with IDs
dogs_db = {
    1: {
        "id": 1,
        "breed": "Labrador",
        "age_limit": 12,
        "description": "Friendly and outgoing, Labs play well with others."
    },
    2: {
        "id": 2,
        "breed": "Beagle",
        "age_limit": 15,
        "description": "Beagles are known for their curious and merry nature."
    },
    3: {
        "id": 3,
        "breed": "Bulldog",
        "age_limit": 10,
        "description": "Bulldogs are calm and courageous, with a friendly demeanor."
    },
    4: {
        "id": 4,
        "breed": "Poodle",
        "age_limit": 14,
        "description": "Poodles are intelligent and easy to train, often excelling in dog sports."
    },
    5: {
        "id": 5,
        "breed": "German Shepherd",
        "age_limit": 13,
        "description": "German Shepherds are loyal, courageous, and confident, often used in service roles."
    },
    6: {
        "id": 6,
        "breed": "Golden Retriever",
        "age_limit": 12,
        "description": "Golden Retrievers are friendly, tolerant, and reliable, making them great family pets."
    },
    7: {
        "id": 7,
        "breed": "Dachshund",
        "age_limit": 16,
        "description": "Dachshunds are curious and brave, known for their unique long body."
    },
    8: {
        "id": 8,
        "breed": "Siberian Husky",
        "age_limit": 14,
        "description": "Huskies are known for their endurance and stamina, with a friendly and mischievous personality."
    },
    9: {
        "id": 9,
        "breed": "Boxer",
        "age_limit": 10,
        "description": "Boxers are playful, energetic, and protective, making them excellent companions."
    },
    10: {
        "id": 10,
        "breed": "Shih Tzu",
        "age_limit": 18,
        "description": "Shih Tzus are affectionate, playful, and outgoing, known for their long, luxurious coat."
    }
}


# Implementation of the gRPC service
class DogService(dog_pb2_grpc.DogServiceServicer): #inheritance from dog_pb2_grpc.DogServiceServicer
    def GetDog(self, request, context):
        dog_data = dogs_db.get(request.id)
        if not dog_data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Dog ID not found")
            return dog_pb2.DogResponse()
        dog = dog_pb2.Dog(
            id=dog_data['id'],
            breed=dog_data['breed'],
            age_limit=dog_data['age_limit'],
            description=dog_data['description']
        )
        return dog_pb2.DogResponse(dog=dog)
def main():
    serve()
    
def serve():
    # Creates a thread pool executor with up to 10 worker threads. This allows the server to handle multiple RPC calls concurrently.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dog_pb2_grpc.add_DogServiceServicer_to_server(DogService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()
