# this file is a service dictionary

from ..main import APP

def save_cover(file) -> str: # file is a MultiDict[Any, Any]

	# TODO: make this safe with secure_filename(file.filename)
	# TODO: make this normed / standardized (same size / quality for all covers?)
	file.save(os.path.join(APP.config['COVER_DIR'], file.file_name))
	return file.file_name
