//Simple QUIZ Game --Written in GOLANG
package main

import "fmt"

func main() {
 fmt.Printf("Welcome to QUIZ!!!!!!\n")
 fmt.Printf("Enter your Name :")
 var name string
 fmt.Scan(&name)
 fmt.Printf("Welcome to Quiz  "+name+"\n" )
 var age uint  
 fmt.Printf("Enter your age ")
 fmt.Scan(&age)
 if age >=10{
	 fmt.Printf("Yes,You can play %v \n",name)
 }else{
	 fmt.Printf("Sorry %v . You cant play\n",name)
	 return
 }
//score and no of questions 
 score:=0
 num_questions:=2
 fmt.Printf("Which Compony own GO \n")
 var answer string 
 fmt.Scan(&answer)
 if answer == "google"{
	 fmt.Printf("Correct !\n")
	 score++
    }else if answer == "Google"{
		fmt.Printf("Correct !")
		score++
    }else if answer == "GOOGLE"{
		fmt.Printf("Correct !\n")
		score++
	}else{
	 fmt.Printf("Incorrect !!\n")
 } 
fmt.Printf("How to create{command} dir in linux :  \t")
var command string
fmt.Scan(&command)
if command == "mkdir"{
	fmt.Printf("correct \n")
	score++
}else{
	fmt.Printf("Sorry!Better Luck Next Time \n")
}

fmt.Printf(" \n You score %v out of  %v \n",score,num_questions)
percentage := (float64(score) / float64(num_questions)) * 100
fmt.Printf("You Scored : %v%% \n",percentage)

} 




