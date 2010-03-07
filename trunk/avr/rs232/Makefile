.PHONY: clean test all help

CFLAGS += -mmcu=atmega128 -I include

vpath %.c src
vpath %.h include

CC = avr-gcc
AR = avr-ar

all: demo-rs232 

demo-rs232: demo-rs232.o librs232.a

demo-rs232.o: demo-rs232.c rs232.h

librs232.a: librs232.a(rs232.o)

rs232.o: rs232.c rs232.h config.h rs232_atmega128.h

test: all
	@echo 
	@echo "####################################################"
	@echo "make sure avrora-beta-1.7.106.jar in your CLASSPATH"
	@echo "test, use 'nc localhost 2930' to capture printf"
	@echo 
	java avrora.Main -monitors=serial -seconds=3 demo-rs232.elf

clean:
	rm -rf *.o *.elf demo-rs232 *.d *.a

help:
	@$(MAKE) --print-data-base -q | \
	    awk '/^[^.%][-A-Za-z0-9_]*:/ \
	    { print substr($$1, 1, length($$1)-1) }' | \
	    sort | \
	    pr --omit-pagination --width=80 --columns=4

depend.d: demo-rs232.c rs232.c
	$(CC) -M $(CFLAGS) $^ >$@

include depend.d


