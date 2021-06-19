package main

import (
	"fmt"
	"os"
	"os/exec"
)

const ARRAY_SIZE = 8
const EMPTY = 0
const BLACK = 1
const WHITE = 2

func initialize_board(ary[ARRAY_SIZE][ARRAY_SIZE] int) [ARRAY_SIZE][ARRAY_SIZE]int {
	ary[3][3] = WHITE
	ary[3][4] = BLACK
	ary[4][3] = BLACK
	ary[4][4] = WHITE
	return ary
}

func put_stone(ary[ARRAY_SIZE][ARRAY_SIZE] int, turn int) (int , int){

	var x, y int
	
	for {
		fmt.Println("input position")
		fmt.Printf("x = ")
		fmt.Scanf("%d" , &x)
		fmt.Printf("y = ")
		fmt.Scanf("%d", &y)

		x = x - 1
		y = y - 1
		if within_range(x, y) && ary[y][x] == EMPTY && check_whole_direction(ary, x, y, turn) {
			clear_terminal_screen()
			break
		}else{
			clear_terminal_screen()
			display_turn(turn)
			display_board(ary)
			fmt.Println("[ERROR] : invalid position.")
		}
	}

	return x, y
}

func change_board(ary[ARRAY_SIZE][ARRAY_SIZE] int, x int, y int, turn int) [ARRAY_SIZE][ARRAY_SIZE]int {

	ary[y][x] = turn
	var direction[3] int = [3]int{-1, 0, 1}

	for _, y_offset := range direction{
		for _, x_offset := range direction {
			ary = turn_over_stone(ary, x, y, x_offset, y_offset, turn)
		}
	}
	return ary
}

func turn_over_stone(ary[ARRAY_SIZE][ARRAY_SIZE] int, x int, y int, x_offset int, y_offset int, turn int) [ARRAY_SIZE][ARRAY_SIZE] int {

	var enemy_color int
	if turn == BLACK {
		enemy_color = WHITE
	} else if turn == WHITE{
		enemy_color = BLACK
	}else {

	}

	if check_direction(ary, x, y, x_offset, y_offset, turn) > 0 {
		x = x + x_offset
		y = y + y_offset
		for within_range(x, y) && ary[y][x] == enemy_color {
			ary[y][x] = turn
			x = x + x_offset
			y = y + y_offset
		}
	}

	return ary
}

func display_turn(turn int) {
	if turn == BLACK {
		fmt.Println(" ---- BLACK TURN ----")
	}else if turn == WHITE {
		fmt.Println(" ---- WHITE TURN ----")
	}else {

	}
}

func display_board(board_ary[ARRAY_SIZE][ARRAY_SIZE] int){

	fmt.Println("   1 2 3 4 5 6 7 8")
	for i:=0; i<ARRAY_SIZE; i++ {
		fmt.Printf(" %d ", i+1)
		for j:=0; j<ARRAY_SIZE; j++ {
			if board_ary[i][j] == EMPTY {
				fmt.Print("□ ")
			}else if board_ary[i][j] == BLACK {
				fmt.Print("○ ")
			}else {
				fmt.Print("● ")
			}
		}
		fmt.Printf("\n")
	}
}

func clear_terminal_screen() {
	c := exec.Command("clear")
	c.Stdout = os.Stdout
	c.Run()
}

func change_turn(turn int) int {

	if turn == BLACK {
		return WHITE
	}else if turn == WHITE {
		return BLACK
	}else {
		return -1
	}
}

func display_result(ary[ARRAY_SIZE][ARRAY_SIZE] int) {

	var black int = 0
	var white int = 0
	for i:=0; i<ARRAY_SIZE; i++ {
		for j:=0; j<ARRAY_SIZE; j++ {
			if ary[i][j] == BLACK {
				black++
			}else if ary[i][j] == WHITE{
				white++
			}else{

			}
		}
	}

	fmt.Println("-----   SCORE   -----")
	fmt.Println(" BLACK:", black, ", WHITE:", white)
	display_board(ary)
	fmt.Println(" ###################")
	if black > white {
		fmt.Println(" # BLACK IS WINNER #")
	}else if white > black {
		fmt.Println(" # WHITE IS WINNER #")
	}else {
		fmt.Println(" #   IT'S A DRAW   #")
	}
	fmt.Println(" ###################")
}


func can_put(ary[ARRAY_SIZE][ARRAY_SIZE] int, turn int)  bool {

	count := 0
	for x_coordinate:=0; x_coordinate<ARRAY_SIZE; x_coordinate++ {
		for y_coordinate:=0; y_coordinate<ARRAY_SIZE; y_coordinate++ {
			count++
			if check_whole_direction(ary, x_coordinate, y_coordinate, turn) {
				return true
			}
		}
	}
	return false
} 

func check_whole_direction(ary[ARRAY_SIZE][ARRAY_SIZE] int, x int, y int, turn int) bool {
	
	var direction[3] int = [3]int{-1, 0, 1}

	for _, y_offset := range direction{
		for _, x_offset := range direction {
			if check_direction(ary, x, y, x_offset, y_offset, turn) > 0 {
				return true
			}
		}
	}
	return false
}

func within_range(x_coordinate int, y_coordinate int) bool {
	if (0 <= x_coordinate) && (x_coordinate <= ARRAY_SIZE-1) && (0 <= y_coordinate) && (y_coordinate <= ARRAY_SIZE-1) {
		return true
	}else {
		return false
	}
}

func check_direction(ary[ARRAY_SIZE][ARRAY_SIZE] int,  x int, y int, x_offset int, y_offset int, turn int) int {
	
	var enemy_color int
	var count int = 0

	if x_offset == 0 && y_offset == 0{
		return 0
	}

	if turn == BLACK {
		enemy_color = WHITE
	} else if turn == WHITE{
		enemy_color = BLACK
	}else {

	}

	x = x + x_offset
	y = y + y_offset
	for within_range(x, y) && ary[y][x] == enemy_color {
		count++
		x = x + x_offset
		y = y + y_offset
	}

	if within_range(x, y){
		if ary[y][x] == turn {
			return count
		}else {
			return 0
		}
	}else {
		return 0
	}
}

func main(){
	
	var turn int = BLACK		// start from black stone
	var x_coordinate, y_coordinate int
	var pass_count int
	var board_array[ARRAY_SIZE][ARRAY_SIZE] int
	
	board_array = initialize_board(board_array)
	clear_terminal_screen()

	for {
		if can_put(board_array, turn) {
			display_turn(turn)
			display_board(board_array)
			x_coordinate, y_coordinate = put_stone(board_array, turn)
			board_array = change_board(board_array, x_coordinate, y_coordinate, turn)
			pass_count = 0
		}else {
			pass_count++
			if pass_count > 2 {
				break
			}
		}
		turn = change_turn(turn)
	}
	display_result(board_array) 
}