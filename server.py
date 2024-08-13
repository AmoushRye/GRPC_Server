import grpc
from concurrent import futures
import dog_pb2
import dog_pb2_grpc

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

def serve():
    # Creates a thread pool executor with up to 10 worker threads. This allows the server to handle multiple RPC calls concurrently.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dog_pb2_grpc.add_DogServiceServicer_to_server(DogService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
