from flask import Flask, request, render_template_string

app = Flask(__name__)

CONFESSION_TEXT = """hii, Kien! i hope u're well and safe while reading this. i just wanted to let this out before this year end, because i just want to move on from this as 2026 starts.
I'm actually planning to this for a while na kaso lagi akong kinakain ng hiya ko kaya di ko matuloy-tuloy. ANYWAYYY, so here's the thing, I know na medyo magiging awkward sa'yo to pero as i said nga, I wanted you know this and let this out. I have a crush on you for quite some time na rin (parang 1st month pa lang natin as classmates ganon). sabi ko dapat happy crush lang kita kaso kasi tumagal yung nararamdaman ko na yun. HUHUHUHU sorry if medyo awkward ako mag-confess kasi di ko to masyadong ginagawa anddd nahihiya talaga ako soferrr. Kung ano mang maging desisyon mo after this confession I'll accept it. Di naman ako nag-confess for you to reciprocate my feelings but rather to let you know my feelings towards you. huhu no pressure at allllll."""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Confession</title>
    <style>
        body {
            background-color: pink;
            background-image:
                radial-gradient(circle at 10% 20%, #ff6f91 8%, transparent 9%),
                radial-gradient(circle at 70% 30%, #ff6f91 6%, transparent 7%),
                radial-gradient(circle at 40% 80%, #ff6f91 7%, transparent 8%),
                radial-gradient(circle at 90% 60%, #ff6f91 6%, transparent 7%),
                radial-gradient(circle at 20% 60%, #ff6f91 8%, transparent 9%);
            background-size: 120px 120px;
            font-family: Arial, sans-serif;
            padding: 30px;
        }

        h1 {
            text-align: center;
        }

        form, .confession, .error {
            background: white;
            padding: 20px;
            max-width: 600px;
            margin: 20px auto;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        input {
            padding: 10px;
            width: 80%;
            font-size: 16px;
        }

        button {
            margin-top: 15px;
            padding: 10px;
            width: 85%;
            background: hotpink;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }

        .confession {
            white-space: pre-wrap;
            text-align: left;
            line-height: 1.6;
        }

        .error {
            color: #d6336c;
        }
    </style>
</head>
<body>

<h1>For U</h1>

{% if show_confession %}
    <div class="confession">
        {{ confession }}
    </div>
{% else %}
    <form method="POST">
        <p>Please enter your name first</p>
        <input type="text" name="name" placeholder="Your name" required>
        <br>
        <button type="submit">Continue</button>
    </form>

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    show_confession = False
    error = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name.lower() == "kien":
            show_confession = True
        else:
            error = "This confession is not for you 🤍"

    return render_template_string(
        HTML_TEMPLATE,
        show_confession=show_confession,
        confession=CONFESSION_TEXT,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

