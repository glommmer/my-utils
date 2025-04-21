import logging
import configparser


def read_config(config_path, encoding=None):
	logging.info(f"config_path: {config_path}")
	config = configparser.ConfigParser()
	config.read(
		filenames=config_path,
		encoding=encoding,
	)
	return config
