# Youtube Spam Detection

### Abstract
 * The ever-growing popularity of YouTube has brought with it a deluge of unwelcome guests: spam comments. These disruptive messages not only detract from user experience but also stifle genuine conversation. While YouTube employs its own filtering system, it often falls short in completely eradicating the problem.
 * This research proposes a novel approach to combating YouTube spam – leveraging the power of ensemble learning. We delve into existing studies on YouTube spam detection and conduct a series of classification experiments. Six individual machine learning algorithms are put to the test: Decision Trees, Bernoulli Naive Bayes, Random Forest, Support Vector Machines (linear). Additionally, we explore the potential of two ensemble models: Ensemble with Hard Voting and Ensemble with Soft Voting. These models combine the strengths of individual algorithms, aiming to achieve a superior level of spam detection accuracy.
 * To comprehensively evaluate these techniques, we train them on a dataset of comments from popular music videos by renowned artists like Psy, Katy Perry, LMFAO, Eminem, and Shakira. By harnessing the capabilities of machine learning and ensemble approaches, this research aims to develop a robust system for filtering YouTube spam comments, fostering a more positive and engaging online platform for users.

### Running the Application
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

#### Running the Application:
  1. Once training is complete, return to your terminal window.
  2. Execute the command:

```bash
py main.py
```

This will launch your application, potentially starting a web server or performing other actions based on your specific implementation.
