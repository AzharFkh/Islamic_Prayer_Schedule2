from flask import Flask, render_template, request
from JDtoJadwalSolat import jadwal_solat, GregorianConverter
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])
        timezone = float(request.form["timezone"])
        altitude = float(request.form["altitude"])
        tanggal = request.form["tanggal"]
        KA = int(request.form["asharMethod"])

        tahun, bulan, hari = map(int, tanggal.split("-"))
        tanggal_obj = datetime.date(tahun, bulan, hari)

        JD_local = GregorianConverter(year=tahun, month=bulan, day=hari).to_JD()
        
        print(JD_local)

        hasil = jadwal_solat(JD_local, latitude, longitude, timezone, altitude, KA=KA, h_subuh=-20, h_isya=-18)

        return render_template(
            "hasil.html",
            hasil=hasil,
            tanggal=tanggal_obj,
            latitude=latitude,
            longitude=longitude,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
