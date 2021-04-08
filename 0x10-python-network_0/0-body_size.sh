#!/bin/bash
#size of body
curl "$1" -sw '%{size_download}\n'
