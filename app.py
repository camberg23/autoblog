import streamlit as st
import openai
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

system_message = """
Your job is to write a full engaging blog post on the relationship between a specific career and personality.

THE SPECIFIC CAREER TO WRITE ABOUT FOR THIS POST IS THE PROFESSION/CAREER OF {PROFESSION}.

### Formatting and content guidelines

#### Title:
- **Format:** Should I Become a {PROFESSION}?

#### Introduction:
- **Tone & Style:** Professional yet relatable, using engaging language and examples from popular culture if applicable.
- **Content Elements:**
  - Briefly romanticize the profession with a cultural or popular reference.
  - State the common misconceptions or oversimplifications about the profession.
  - Emphasize the importance of aligning personality with career choice.

#### What does a {PROFESSION} do?
- **Structure:**
  - Provide a broad definition followed by specific daily tasks and responsibilities.
  - Use subheadings for clarity if necessary.
  - Highlight the variety within the profession to acknowledge different specializations or roles.

#### What are the skills needed to become a {PROFESSION}?
- **List Format:**
  - Enumerate and detail the key skills required, such as communication, analytical thinking, technical skills, etc.
  - Include both hard (technical) and soft (interpersonal) skills.
  - Each skill should be explained with examples of how it's applied in the profession.

#### Which personality types make the best {PROFESSION}s?
- **Approach:**
  - Describe how certain personality traits may benefit individuals in the profession.
  - Use the Big Five personality traits and Myers-Briggs Type Indicators (MBTI) as references to link personality with professional aptitude.
  
#### Big Five personality traits of {PROFESSION}s:
- **Content Development:**
  - For each of the Big Five traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism), describe how they might manifest in successful professionals in the field.
  - Provide examples and professional scenarios where these traits would be advantageous.
  - Link to the relevant Truity page for each trait.

#### TypeFinder types of {PROFESSION}s:
[SPECIAL NOTE: we call MBTI/Myers-Briggs types 'TypeFinder' types! Use the same acronyms and theory [eg, INTP], but call them TypeFinder types, NOT MBTI or Myers-Briggs]
- **Detailed Analysis:**
  - Discuss how various TypeFinder types may find different aspects of the profession more suitable or challenging.
  - Offer insights into which TypeFinder types commonly excel and why, including potential career paths within the profession for different types.
  - Link to Truity’s TypeFinder type descriptions for deeper exploration.

#### How to get started becoming a {PROFESSION}:
- **Guidance:**
  - Suggest initial steps for exploration, such as internships, educational paths, entry-level jobs, or mentorship opportunities.
  - Mention any relevant aptitude tests or career assessments that might help guide decision-making, including a call-to-action to take such assessments.
  - Encourage self-reflection and research as key components to making an informed career choice.

#### Closing Remarks:
- **Positive Reinforcement:**
  - Affirm that every personality has unique potential within the profession.  - Encourage readers to find their niche or specialization that aligns with their personality and skills.
  - Close with an empowering statement or a call-to-action to take the next step in exploring the profession.
  

Be sure to include all of the following links somewhere in the body of the text wherever it makes the most sense:
-Career personality profiler test: https://www.truity.com/test/career-personality-profiler-test 
TypeFinder (MBTI) test: https://www.truity.com/test/type-finder-personality-test-new
Big Five test: https://www.truity.com/test/big-five-personality-test 

FORMAT THE BLOG IN MARKDOWN!

THE ENTIRE BLOG SHOULD BE APPROXIMATELY 1500 WORDS. THIS IS A CRITICAL REQUIREMENT.
BE SURE NOT TO MAKE IT TOO SHORT! YOU WILL NOT RUN OUT OF TOKENS AT THIS LENGTH!
"""
API = st.secrets['API']
def generate_blog(profession):
    # Assuming ChatOpenAI, LLMChain, and PromptTemplate are imported from a module or defined elsewhere
    chat_model = ChatOpenAI(openai_api_key=API, model_name='gpt-4', temperature=0.25, max_tokens=7000)
    chat_chain = LLMChain(prompt=PromptTemplate.from_template(system_message), llm=chat_model)
    return chat_chain.run(PROFESSION=profession)

# Streamlit app
st.title("Profession Blog Generator")

# User input
profession = st.text_input("Enter a profession", "")

# Button to generate blog
if st.button("Generate Blog"):
    with st.spinner("Please wait, this might take a minute..."):
        # Generate blog
        blog_post = generate_blog(profession)
        # Display blog post with markdown formatting
        st.markdown(blog_post, unsafe_allow_html=True)