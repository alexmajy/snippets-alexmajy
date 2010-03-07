.PHONY: clean test all

CFLAGS += -mmcu=atmega128 -I include
LDFLAGS += -mmcu=atmega128

vpath %.c src
vpath %.h include

CC = avr-gcc
AR = avr-ar


all: demo-rs232

demo-rs232: demo-rs232.o librs232.a

demo-rs232.o: demo-rs232.c rs232.h

librs232.a: librs232.a(rs232.o)

rs232.o: rs232.c rs232.h config.h rs232_atmega128.h

define avrora-test
cp $< $<.elf
echo 
echo "####################################################"
echo "make sure avrora-beta-1.7.106.jar in your CLASSPATH"
echo -n "current CLASSPATH="
echo $$CLASSPATH
echo "test, use 'nc localhost 2930' to capture printf"
echo 
java avrora.Main -monitors=serial -seconds=3 $<.elf
rm -rf $<.elf
endef

test: demo-rs232
	@$(avrora-test)


clean:
	rm -rf *.o *.elf demo-rs232 *.d *.a

-include depend.d

depend.d: demo-rs232.c rs232.c
	$(CC) -M $(CFLAGS) $^ >$@


