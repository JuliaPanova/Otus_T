from app import app

app.config.update(
    DEBUG=True,
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
