package main

import (
	"fmt"
	"log"
	"net/http"
)

func starHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/star" {
		http.Error(w, "404 not found", http.StatusNotFound)
		return
	}
	if r.Method != "GET" {
		http.Error(w, "method is not supported", http.StatusNotFound)
		return
	}
	http.ServeFile(w, r, "./static/star.html")
}

func formHandler(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseForm(); err != nil {
			// err := r.ParseForm()은 r.ParseForm() 함수의 반환 값을 변수 err에 할당하고, 해당 변수를 통해 오류를 확인합니다. 만약 폼 데이터를 구문 분석하는 과정에서 오류가 발생하면 err 변수에 오류 정보가 저장됩니다.
		// r.ParseForm() 함수는 요청의 바디(body)를 읽어와 폼 데이터를 구문 분석합니다. 만약 구문 분석 과정에서 오류가 발생하면, 예를 들어 잘못된 폼 데이터 형식이거나 요청 바디를 읽을 수 없는 경우 등, err 변수에 오류 정보가 저장됩니다.
		fmt.Fprintf(w, "ParseFoem() err: %v", err)
		return
	}
	fmt.Fprintf(w, "POST request successful\n")
	vote_name := r.FormValue("vote_name")
	vote_result := r.FormValue("vote_result")
	fmt.Fprintf(w, "Vote_name = %s\n", vote_name)
	fmt.Fprintf(w, "Vote_result = %v\n", vote_result)
}

func main() {
	fileServer := http.FileServer(http.Dir("./static"))
	http.Handle("/", fileServer)
	http.HandleFunc("/form", formHandler)
	http.HandleFunc("/star", starHandler)

	fmt.Println("Starting server at port 8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}