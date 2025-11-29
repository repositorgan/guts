**AI DOCUMENT SUMMARIZER**
_This is a simple and fast tool that reads long text, (.txt), files and returns to you a short 1–2 sentence summary. Showcases Python skills in constructing useful tools._

_The tool provides keyword scoring to identify the most important ideas in the document and returns 1-2 sentences with the most important content to takeaway from each file._

_Summarizer is perfect for analysts, developers, and teachers. Saves time and money in labor of interpretation and understanding of larger bulk text data. Provides option to save a new .txt file of final product._

**USAGE**
**PRODUCE SUMMMARY**
_python -m summarizer example.txt_
**VERBOSE MODE**
_python -m summarizer example.txt -v_
**SAVE TO A FILE**
_python -m summarizer example.txt -o output.txt_

**HOW IT WORKS**

 _______________________________
|    Input text, (.txt), file   |
|-------------------------------|
| Full length analysis or report|

                |
                V
                |
                V
                |
                V
 _________________________________
|      SUMMARIZER PROCESS        |
|--------------------------------|
|   1. Split text into sentences |
|   2. Count keyword frequencies |
|   3. Skips common words         |
|   4. Score each sentence       |
|   5. Pick top 1-2 sentences    |
|________________________________|
                |
                V
                |
                V
                |
                V
 __________________________________
|           FINAL OUTPUT           |
|----------------------------------|
|     Top scoring 1-2 sentences    |
|        Keywords identified       |
|       Option to save output      |
|__________________________________|

**INSTALLATION**
Clone the repository:
_git clone https://github.com/tech-debt/AI-Document-Summarizer.git_


