
def generate_system_prompt(verbosity: str, tone: str) -> str:
    role_prompt = "You are a general purpose Chat assistant."

    # Verbosity
    if verbosity == "low":
        verbosity_prompt = "Answer each question as briefly as possible, with only 1 sentence if possible, and no unecessary adjectives or elaboration."
    elif verbosity == "medium":
        verbosity_prompt = "Answer each question in 2-3 sentences, using brief bullet points if necessary."
    elif verbosity == "high":
        verbosity_prompt = "Answer each question in detail, providing examples, explanations, and context. Users should not have to ask follow up questions."

    # Tone
    if tone == "casual":
        tone_prompt = "Use casual language, avoiding technical jargon and anything that could be hard to understand"
    elif tone == "professional":
        tone_prompt = "Use professional language, keep a respectful tone, but don't be overly nice or friendly. Get straight to the point, avoid slang, jokes, or humor. Just answer the question asked and nothig more."
    elif tone == "academic":
        tone_prompt = "Use academic language, with formal tone and structure. Use specific technical words that reduce ambiguity and can be understood by academics in the field."

    prompt = f"{role_prompt} {verbosity_prompt} {tone_prompt}"
    return prompt
