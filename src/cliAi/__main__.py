import typer
import math

app = typer.Typer(help="CLI tool for mathematical operations")

@app.command("sqrt")
def square_root(number: float = typer.Argument(..., help="The number to calculate square root of")):
    """Calculate the square root of a number."""
    result = math.sqrt(number)
    print(f"Square root of {number} is {result}")

@app.command("prime")
def is_prime(number: int = typer.Argument(..., help="Check if this number is prime")):
    """Check if a number is prime."""
    if number <= 1:
        print(f"{number} is not a prime number")
        return
        
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number")
            return
            
    print(f"{number} is a prime number")

@app.command("factorial")
def factorial(number: int = typer.Argument(..., help="Calculate factorial of this number")):
    """Calculate the factorial of a number."""
    if number < 0:
        print("Factorial is not defined for negative numbers")
        return
        
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")

@app.command("primes")
def list_primes(limit: int = typer.Argument(..., help="List all prime numbers up to this limit")):
    """List all prime numbers up to a given limit."""
    if limit < 2:
        print("No prime numbers in the given range")
        return
        
    primes = []
    for num in range(2, limit + 1):
        is_num_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_num_prime = False
                break
        if is_num_prime:
            primes.append(num)
            
    print(f"Prime numbers up to {limit}: {primes}")

@app.command("gcd")
def greatest_common_divisor(a: int = typer.Argument(..., help="First integer"),
                           b: int = typer.Argument(..., help="Second integer")):
    """Calculate the greatest common divisor of two integers."""
    result = math.gcd(a, b)
    print(f"GCD of {a} and {b} is {result}")

@app.command("lcm")
def least_common_multiple(a: int = typer.Argument(..., help="First integer"),
                         b: int = typer.Argument(..., help="Second integer")):
    """Calculate the least common multiple of two integers."""
    result = abs(a * b) // math.gcd(a, b)
    print(f"LCM of {a} and {b} is {result}")

def main():
    app()

if __name__ == "__main__":
    main()