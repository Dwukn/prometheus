// original name was tic_tac_toe but wont work cause apperenty rust needs main.rs to run

use std::io::{self, Write};

#[derive(Clone, Copy, PartialEq, Debug)]
enum Player {
    X,
    O,
}

#[derive(Clone)]
struct Game {
    board: [[Option<Player>; 3]; 3],
    current_player: Player,
}

impl Game {
    fn new() -> Game {
        Game {
            board: [[None, None, None], [None, None, None], [None, None, None]],
            current_player: Player::X,
        }
    }

    fn print_board(&self) {
        for row in &self.board {
            for cell in row {
                match cell {
                    Some(Player::X) => print!(" X "),
                    Some(Player::O) => print!(" O "),
                    None => print!(" . "),
                }
            }
            println!();
        }
    }

    fn play_turn(&mut self, row: usize, col: usize) -> Result<(), String> {
        if row >= 3 || col >= 3 {
            return Err("Invalid move, out of bounds.".to_string());
        }

        if self.board[row][col].is_some() {
            return Err("Cell already taken.".to_string());
        }

        self.board[row][col] = Some(self.current_player);
        self.switch_player();
        Ok(())
    }

    fn switch_player(&mut self) {
        self.current_player = match self.current_player {
            Player::X => Player::O,
            Player::O => Player::X,
        };
    }

    fn check_winner(&self) -> Option<Player> {
        // Check rows and columns
        for i in 0..3 {
            if let Some(player) = self.board[i][0] {
                if self.board[i][1] == Some(player) && self.board[i][2] == Some(player) {
                    return Some(player);
                }
            }

            if let Some(player) = self.board[0][i] {
                if self.board[1][i] == Some(player) && self.board[2][i] == Some(player) {
                    return Some(player);
                }
            }
        }

        // Check diagonals
        if let Some(player) = self.board[0][0] {
            if self.board[1][1] == Some(player) && self.board[2][2] == Some(player) {
                return Some(player);
            }
        }

        if let Some(player) = self.board[0][2] {
            if self.board[1][1] == Some(player) && self.board[2][0] == Some(player) {
                return Some(player);
            }
        }

        None
    }

    fn is_draw(&self) -> bool {
        self.board.iter().all(|row| row.iter().all(|&cell| cell.is_some()))
    }
}

fn main() {
    let mut game = Game::new();
    let mut input = String::new();

    loop {
        game.print_board();

        // Get the current player's move
        println!("\nPlayer {:?}, enter your move (row and column): ", game.current_player);

        input.clear();
        print!("Row: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let row: usize = input.trim().parse().unwrap_or(0);

        input.clear();
        print!("Column: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let col: usize = input.trim().parse().unwrap_or(0);

        match game.play_turn(row, col) {
            Ok(_) => {
                if let Some(winner) = game.check_winner() {
                    game.print_board();
                    println!("\nPlayer {:?} wins!", winner);
                    break;
                } else if game.is_draw() {
                    game.print_board();
                    println!("\nThe game is a draw.");
                    break;
                }
            }
            Err(e) => println!("{}", e),
        }
    }
}
