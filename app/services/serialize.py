from dicttoxml import dict_to_xml
from json import dumps as dict_to_json
from flask import Response as Res

def to_json(o) -> str:
	return dict_to_json(o)

def to_xml(o) -> str:
	return dict_to_xml(o)

def respond(req, data):
	if "json" in req.content_type:
		return Res(to_json(data), status=200, mimetype="application/json", content_type="text/json; charset=utf-8")
	elif "xml" in req.content_type:
		return Res(to_json(data), status=200, mimetype="application/xml", content_type="text/xml; charset=utf-8")
	# TODO: handle input errors
	# else:
	# 	return 