.PHONY: clean test all 

CFLAGS += -mmcu=atmega128 

CC = avr-gcc

all: demo-rs232.elf 

demo-rs232.elf: demo-rs232.c rs232.o 
	$(CC) $(CFLAGS) $^ -o $@

rs232.o: rs232.c rs232.h config.h rs232_atmega128.h
	$(CC) -c $(CFLAGS) $<

test: all
	@echo 
	@echo "####################################################"
	@echo "make sure avrora-beta-1.7.106.jar in your CLASSPATH"
	@echo "test, use 'nc localhost 2930' to capture printf"
	@echo 
	java avrora.Main -monitors=serial -seconds=3 demo-rs232.elf

clean:
	rm -rf *.o *.elf

