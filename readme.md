# Mathematical CLI Tool

A command-line interface for various mathematical operations, built with Typer.

## Installation

```bash
pip install cliAi
```

Or, if installing from source:

```bash
git clone https://github.com/yourusername/Lab_Agentic_Tests.git
cd Lab_Agentic_Tests
pip install -e .
```

## Usage

This CLI tool provides several mathematical functions accessed through subcommands.

### Square Root

Calculate the square root of a number:

```bash
cliAi sqrt 16
# Output: Square root of 16.0 is 4.0

cliAi sqrt 2
# Output: Square root of 2.0 is 1.4142135623730951
```

### Prime Number Check

Determine if a number is prime:

```bash
cliAi prime 17
# Output: 17 is a prime number

cliAi prime 15
# Output: 15 is not a prime number
```

### Factorial

Calculate the factorial of a number:

```bash
cliAi factorial 5
# Output: Factorial of 5 is 120

cliAi factorial 0
# Output: Factorial of 0 is 1
```

### List Prime Numbers

Generate a list of all prime numbers up to a specified limit:

```bash
cliAi primes 20
# Output: Prime numbers up to 20: [2, 3, 5, 7, 11, 13, 17, 19]
```

### Greatest Common Divisor (GCD)

Find the greatest common divisor of two integers:

```bash
cliAi gcd 48 18
# Output: GCD of 48 and 18 is 6
```

### Least Common Multiple (LCM)

Find the least common multiple of two integers:

```bash
cliAi lcm 12 18
# Output: LCM of 12 and 18 is 36
```

## Help

Each command has a help option that explains its purpose and required arguments:

```bash
cliAi --help
# Shows general help and lists all available commands

cliAi sqrt --help
# Shows help specific to the sqrt command
```

## Requirements

- Python 3.6+
- typer[all]

## License

This project is licensed under the MIT License - see the LICENSE file for details.