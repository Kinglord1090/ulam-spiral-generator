# Ulam Spiral Generator 🔢

This project generates artistic patterns by plotting prime numbers in a spiral form a.k.a. Ulam Spiral using Python's `turtle` module. The art is created by checking if a number is prime and stamping a shape if true, with the color gradually shifting through a spectrum. The project explores two primary shapes—square spirals and circular spirals—selected randomly at runtime.

## Features

- **Prime Number Visualization**: Plots shapes at positions corresponding to prime numbers, creating visually appealing patterns.
- **Color Gradation**: Uses HSV color space to shift colors smoothly, enhancing the aesthetic of the generated art.
- **Randomized Shape Selection**: Supports multiple turtle shapes (`circle`, `square`, `triangle`, `turtle`, `classic`), selected randomly for each run.
- **Dual Spiral Modes**: Generates either square spirals or circular spirals based on a random choice.
- **Efficient Prime Check**: Optimized prime-checking to reduce redundant calculations.
- **Customizability**: Simple to adjust color transition speed, shape size, and pattern density.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ulam-spiral-generator.git
    ```
2. Install the required Python libraries:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project folder:
    ```bash
    cd ulam-spiral-generator
    ```
2. Run the script:
    ```bash
    python ulam-spiral-gen.py
    ```
3. The program will randomly select a shape and a spiral mode (square or circle).
4. Watch the art unfold as prime numbers are plotted with shifting colors.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ## Acknowledgments

- Inspired by the beauty of prime numbers and the work of Stanislaw Ulam, creator of the Ulam Spiral.  
- Uses `colorsys` for smooth HSV to RGB color transitions.
