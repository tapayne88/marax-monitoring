#! /bin/sh

APPROX_5_MINS_DATA=750

tail --lines $APPROX_5_MINS_DATA $1 | tac
