
# Optimizer Algorithms: A Comparative Study

This project investigates various optimization algorithms used in training deep neural networks. It specifically focuses on Stochastic Gradient Descent (SGD), Momentum, Nesterov Accelerated Gradient, and the Adam optimizer.

## Overview

The goal of this research was to gain a deeper understanding of the mathematical formulations behind popular optimization algorithms and evaluate their performance on a real-world dataset. The following tasks were accomplished:

1. Researched and documented 13 mathematical formulae underlying the functioning of SGD, Momentum, Nesterov, and Adam optimizers.
2. Implemented these optimizers in Python and simulated their behavior on the MNIST dataset, training a 3-layer neural network for 30 epochs using mean squared error as the loss function.
3. Compared the accuracy and training time of the optimizers, concluding that the Adam optimizer achieved 7% higher accuracy than SGD, despite an 11% increase in training time.
4. Co-authored and presented a research paper to 35 students, highlighting the real-world advantages and trade-offs of the studied optimizers.

## Results

The key findings of this study are:

- The Adam optimizer demonstrated the best performance, achieving an accuracy of 97% on the MNIST dataset after 30 epochs.
- SGD, despite being simple and computationally efficient, lagged behind Adam in terms of accuracy (90%).
- Momentum and Nesterov Accelerated Gradient optimizers exhibited improved convergence rates compared to vanilla SGD but did not outperform Adam.
- The computational overhead of Adam was found to be reasonable, with an 11% increase in training time compared to SGD.

## Usage

The project includes Python scripts for implementing the optimizers and running the simulations on the MNIST dataset. To replicate the results, follow these steps:

1. Clone the repository: `git clone https://github.com/your-repo/optimizer-study.git`
2. Explore the different notebooks corresponding to the various optimizers. 

This will train the neural network using each optimizer and log the accuracy and training time results.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to thank our professors and fellow students for their guidance and feedback throughout this research project.
