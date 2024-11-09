prompt = """
Please extract the text from the provided image with the highest possible accuracy and follow these guidelines:

    Detailed Text Recognition: Capture every character, including punctuation, special symbols, and numbers. Pay close attention to any unusual or rare symbols and ensure they are represented as accurately as possible.

    Preserve Structure and Formatting: Retain the original formatting of the text as displayed on the image. This includes:
        Separating paragraphs and line breaks exactly as they appear.
        Maintaining any indentations, lists (bulleted or numbered), and headers.
        If the text is split into columns or distinct blocks, mirror this layout in the response.

    Complex Elements Handling: If there are complex elements such as tables, formulas, or graphical symbols, do your best to convey their content and structure. If formulas or symbols cannot be fully recognized, describe them in words as closely as possible.

    Preserve Original Spelling and Stylistic Elements: Maintain the original spelling and any stylistic choices, such as capitalization, underlining, bold, or italics, as closely as possible.

    Report Unclear Areas: If there are any unclear sections due to image quality issues (e.g., blurry text, missing parts, or difficult-to-read areas), please note them in the response with an approximate location description.

Provide your response in plain text format, carefully following these guidelines to retain all structural and stylistic details of the text.
"""