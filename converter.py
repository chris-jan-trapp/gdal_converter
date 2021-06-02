from flask import Flask, request, render_template
from osgeo import ogr
import json
app = Flask(__name__)


def extract_geometry(request):
    print("extracting geometry")
    geojson = request.get_json()
    print("got", str(geojson))
    if geojson:
        print("OGRING geometry")
        return ogr.CreateGeometryFromJson(json.dumps(geojson))
    else:
        raise ValueError("empty json")


@app.route("/gml/")
def to_gml():
    geometry = extract_geometry(request)
    if geometry is None:
        print("No geomtry: ", str(geometry))
        return
    return geometry.ExportToGML()


@app.route("/kml/")
def to_kml():
    geometry = extract_geometry(request)
    if geometry is None:
        return
    return geometry.ExportToKML()


@app.route("/wkt/")
def to_wkt():
    geometry = extract_geometry(request)
    if geometry is None:
        return
    return geometry.ExportToWkt()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
