package main

import (
	"context"
	"log"
	"net"

	pb "realtime/proto"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedRealtimeServiceServer
}

func (s *server) SendMessage(ctx context.Context, req *pb.MessageRequest) (*pb.MessageResponse, error) {
	log.Printf("Received: %s", req.Message)
	return &pb.MessageResponse{Reply: "Message received: " + req.Message}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterRealtimeServiceServer(grpcServer, &server{})

	log.Println("gRPC server is running on port 50051")
	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
