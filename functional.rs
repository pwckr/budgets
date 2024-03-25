// All functions return `finite data structures`.
// They also have a fixed size when compiling/running.

// Functional aspects addressed:
// Recursion
fn factorial(n: u64) -> u64 {
    if n == 0 {
        1
    } else {
        n * factorial(n - 1)
    }
}

// Functional aspects addressed:
// Higher-order function
// Function as parameter `|&x| x % 2 == 0``
// Closure with `|&x| x % 2 == 0``
// Also `|&x| x % 2 == 0` is anonymous
fn filter_even(numbers: Vec<i32>) -> Vec<i32> {
    numbers.into_iter().filter(|&x| x % 2 == 0).collect()
}

// Functional aspects addressed:
// - Higher-order function `map`
// - Closure within map function call `|x| x.pow(2)`
// - Anonymous function `|x| x.pow(2)` because its inline

fn sum_of_squares(numbers: Vec<i32>) -> i32 {
    numbers.into_iter().map(|x| x.pow(2)).sum()
}


fn main() {
    let numbers = vec![1, 2, 3, 4, 5];

    println!("Factorial of 5: {}", factorial(5));
    println!("Even numbers: {:?}", filter_even(numbers));
    println!("Sum of squares: {}", sum_of_squares(vec![1, 2, 3, 4, 5]));
}
