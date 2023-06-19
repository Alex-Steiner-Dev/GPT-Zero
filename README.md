<h1>GPT-Zero</h1>

<p>A recreation of the website <a href="https://gptzero.me">gptzero.me</a> which utilizes the OpenAI GPT-2 model to determine whether a piece of text was written by a human or a machine. This program allows you to input a piece of text and it will output a score indicating the likelihood that the text was written by a human.</p>

<h2>Getting Started</h2>

<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h3>Prerequisites</h3>

<ul>
  <li>Python 3.9 or higher</li>
  <li>The OpenAI library</li>
  <li>NLPT (Natural Language Toolkit)</li>
  <li>Flask (Web framework)</li>
</ul>

<h3>Installing</h3>

<p>To install the necessary libraries, run the following command in your terminal:</p>
<code>pip install openai nltk flask</code>
<p>This command will install the OpenAI library, NLTK, and Flask. The OpenAI library is used to access the GPT-2 model and perform the text generation and scoring. NLTK is used for natural language processing tasks such as tokenization and stemming. Flask is used to create the web interface for the program.</p>

<h3>Running the program</h3>

<p>To run the program, simply type the following command in your terminal:</p>
<code>./run.sh</code>
<p>This will start the local server and the program can be accessed in your web browser at <a href="http://localhost:8080/">http://localhost:8080/</a></p>

<p>You can input a text in the text area and click on "Submit" button. The program will use the GPT-2 model to generate a similar text and compare the input text with the generated text, based on this it will output a score indicating the likelihood that the text was written by a human.</p>

<h2>Built With</h2>

<ul>
  <li><a href="https://www.python.org/">Python</a> - Programming language</li>
  <li><a href="https://openai.com/">OpenAI</a> - AI library</li>
  <li><a href="https://www.nltk.org/">NLTK</a> - Natural Language Toolkit</li>
  <li><a href="https://flask.palletsprojects.com/en/2.1.x/">Flask</a> - Web framework</li>
</ul>

<h2>Author</h2>

<ul>
  <li>Alex Steiner - <a href="https://github.com/AlexSteiner30">GitHub</a></li>
</ul>

<h2>Acknowledgments</h2>
<ul>
  <li>Inspiration from <a href="https://gptzero.me">gptzero.me</a></li>
</ul>
<p>Additionally, please note that to run this model you need to have credentials to access OpenAI's GPT2 model. You can find more information on how to acquire credentials on the <a href="https://openai.com/">OpenAI website</a>.</p>
