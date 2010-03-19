.PHONY: clean test-foo

#Ensure the correct enviornment exists
#CILPATH = $HOME/cil-1.3.7
ifndef CILPATH
$(error Must define CILPATH environment, e.g. export CILPATH=$$HOME/cil-1.3.7  )
endif

LIBS := unix str cil
C_FILES := foo.c

INCDIRS = $(CILPATH)/obj/x86_LINUX

MAIN := cil001_demo
CMOS := 

$(MAIN): $(MAIN).cmo $(CMOS)
	ocamlc -I $(INCDIRS) $(addsuffix .cma,$(LIBS)) $(CMOS) -o $@ $< 

#lis.cmo: lowlog.cmo

%.cmo: %.ml
	ocamlc -c -I $(INCDIRS) $^

%.i: %.c
	cpp $^ >$@

test-foo: $(C_FILES:.c=.i)
	./$(MAIN) $^


clean:
	rm -f *.cm? *.i
	rm -f $(MAIN)


