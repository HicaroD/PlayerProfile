from flask import Flask, jsonify, make_response
import scraper

app = Flask(__name__)

@app.route("/<nickname>")
def get_player(nickname):
    liquipedia_scraper = scraper.LiquipediaScraper(nickname)
    player_description = {
            "description": liquipedia_scraper.get_player_description(),
    }
    return make_response(jsonify(player_description))

if __name__ == "__main__":
    app.run()
