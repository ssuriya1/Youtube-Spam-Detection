# YouTube Spam Comment Detection using Ensemble Learning

### Abstract
 * The ever-growing popularity of YouTube has brought with it a deluge of unwelcome guests: spam comments. These disruptive messages not only detract from user experience but also stifle genuine conversation. While YouTube employs its own filtering system, it often falls short in completely eradicating the problem.
 * This research proposes a novel approach to combating YouTube spam – leveraging the power of ensemble learning. We delve into existing studies on YouTube spam detection and conduct a series of classification experiments. Six individual machine learning algorithms are put to the test: Decision Trees, Bernoulli Naive Bayes, Random Forest, Support Vector Machines (linear). Additionally, we explore the potential of two ensemble models: Ensemble with Hard Voting and Ensemble with Soft Voting. These models combine the strengths of individual algorithms, aiming to achieve a superior level of spam detection accuracy.
 * To comprehensively evaluate these techniques, we train them on a dataset of comments from popular music videos by renowned artists like Psy, Katy Perry, LMFAO, Eminem, and Shakira. By harnessing the capabilities of machine learning and ensemble approaches, this research aims to develop a robust system for filtering YouTube spam comments, fostering a more positive and engaging online platform for users.

### Introduction

YouTube's immense popularity has unfortunately become a breeding ground for disruptive spam comments. These messages not only degrade user experience but also hinder meaningful conversations. While YouTube's built-in filtering system offers some protection, it frequently falls short of eliminating the issue entirely.

This project tackles the challenge of YouTube spam comment detection by leveraging the power of ensemble learning, a machine learning technique that combines the strengths of multiple algorithms to achieve enhanced performance.

### Methodology

1. **Literature Review:** We conducted a thorough review of existing research on YouTube spam comment detection to understand current approaches, identify strengths and limitations, and establish a foundation for our own investigation.

2. **Data Acquisition and Preprocessing:**
    * Dataset: A comprehensive dataset of comments was collected from popular music videos by well-known artists to ensure a representative sample of YouTube comment content.
    * Preprocessing: The comments were meticulously cleaned and preprocessed to transform them into a suitable format for machine learning algorithms. This may involve techniques like stemming, lemmatization, stop word removal, and other text normalization steps.

3. **Machine Learning Models:** The following individual machine learning algorithms were evaluated for their effectiveness in detecting YouTube spam:
    * Decision Trees
    * Bernoulli Naive Bayes
    * Random Forest
    * Support Vector Machines (linear)

4. **Ensemble Learning:** We explored the potential of two ensemble models to potentially surpass the performance of individual algorithms:
    * Ensemble with Hard Voting: Combines predictions from each model through majority vote classification.
    * Ensemble with Soft Voting: Aggregates predictions from each model by averaging their predicted probabilities.

5. **Evaluation:** All models underwent rigorous training and evaluation to assess their accuracy, precision, recall, and F1-score metrics in detecting YouTube spam comments.

### Conclusion

Summarize the project's overall contribution to the field of YouTube spam comment detection. Did ensemble learning deliver the anticipated improvements? Emphasize the potential for this approach to be integrated into real-world YouTube spam filtering systems.

# Running the Application

**Prerequisites:**
 * Python (version 3.10.8 recommended)
 * Code Editor (any preferred editor)

#### Installation:

  1. Open a terminal window.
  2. Ensure you have pip installed (usually included with Python).
  3. Run the following command to install the required libraries:


```bash
pip install pandas numpy nltk scikit-learn matplotlib joblib Flask reportlab selenium
```

#### Dataset Generation (Optional):

If you need to generate a dataset for training, follow these steps:
  1.In your terminal, execute the command:

```bash
py dataset.py
```
This script will likely create a CSV file containing the dataset. Double-check the generated file and adjust the training script if needed.

#### Training and Testing (Using Jupyter Notebook):

  1. Open the training.ipynb file in your preferred code editor or Jupyter Notebook environment. Consider using VS Code with the Jupyter extension for a seamless experience.
  2. Important: Before training, verify the generated dataset's CSV file path in the training.ipynb file. Replace any placeholders with the actual location.
  3. Run the Jupyter Notebook cells one by one (typically using Shift+Enter) to execute the training and testing code. This usually involves splitting data (80% training, 20% testing), training the model, and evaluating its performance.

### Recomended Extensions for VSCode

  1. [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) - Pack Includes (Jupyter keymaps, Jupyter Notebook renderer, Jupyter slideshow, Jupyter cell tags).
  2. [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - Helps for writing code in vscode.
  3. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - supports for python language and helps pylance to IntelliSense, linting, codenavigation.
  4. [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) - used for debugging python application.
  5. [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) - used for formatting python code.

#### Running the Application:

  1. Once training is complete, return to your terminal window.
  2. Execute the command:

```bash
py main.py
```

This will launch your application, potentially starting a web server or performing other actions based on your specific implementation.
