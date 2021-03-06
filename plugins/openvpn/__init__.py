# coding=utf-8
"""OpenVPN Plugin for Genesis"""
MODULES = ['main', 'widget', 'config', 'backend', ]

DEPS = [
	(['any'],
	[
		('app', 'openvpn', 'openvpn'),
	])
]

NAME = 'OpenVPN'
PLATFORMS = ['any']
DESCRIPTION = 'OpenVPN Management'
VERSION = '1.1'
GENERATION = 1
AUTHOR = 'Ilya Voronin'
HOMEPAGE = 'https://github.com/ivoronin'
