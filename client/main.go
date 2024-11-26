package main

import (
	"context"
	"fmt"
	"io"
	"os"
	"time"

	"github.com/www-printf/virtual-printer/client/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	client := proto.NewVirtualPrinterClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second*5)
	defer cancel()

	pdfFile, err := os.OpenFile("test.pdf", os.O_RDONLY, 0)
	if err != nil {
		panic(err)
	}
	content, err := io.ReadAll(pdfFile)
	if err != nil && err != io.EOF {
		panic(err)
	}

	resp, err := client.SubmitPrintJob(ctx, &proto.PrintDocument{
		DocumentId: "123",
		Content:    content,
		Settings: &proto.PrintSettings{
			ColorMode:   proto.PrintSettings_COLOR_MODE_GRAYSCALE,
			PaperSize:   proto.PrintSettings_PAPER_SIZE_A4,
			Orientation: proto.PrintSettings_ORIENTATION_PORTRAIT,
			Copies:      2,
			DoubleSided: false,
		},
	})
	if err != nil {
		panic(err)
	}

	println("Print job submitted successfully with job id: ", resp.JobId)

	time.Sleep(time.Second * 3)

	jobStatus, err := client.GetJobStatus(ctx, &proto.GetJobStatusRequest{
		JobId: resp.JobId,
	})
	if err != nil {
		panic(err)
	}
	fmt.Printf("Job status: %v\n", jobStatus)

	queuedJobs, err := client.ListPrintJobs(ctx, &proto.Empty{})
	if err != nil {
		panic(err)
	}
	fmt.Printf("Queued jobs: %v\n", queuedJobs.GetJobs())
}
