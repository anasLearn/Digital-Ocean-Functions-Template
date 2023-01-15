#!/bin/bash

set -e

ROOT_FOLDER=.
TARGET_FOLDER=$ROOT_FOLDER/packages/pos-notif/routine

cp -R  $ROOT_FOLDER/src $ROOT_FOLDER/settings $ROOT_FOLDER/requirements.txt $TARGET_FOLDER