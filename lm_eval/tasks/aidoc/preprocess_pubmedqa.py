def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    return "Abstract: {}\nQuestion: {}\nThe answer is:".format(
        ctxs,
        doc["QUESTION"],
    )
