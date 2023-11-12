# cocotb setup
# MODULE = test.test_alu_arithmetic, test.test_alu_logic, test.test_alu_byte, test.test_alu_rotation
MODULE = test.test_alu_arithmetic, test.test_alu_logic, test.test_alu_byte, test.test_alu_rotation
export MODULE
TOPLEVEL = tb
VERILOG_SOURCES = tb.v

include $(shell cocotb-config --makefiles)/Makefile.sim

synth_alu:
	yosys -p "read_verilog alu.v; proc; opt; show -colors 2 -width -signed alu"

test_alu:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s tb -s dump -g2012 dump_alu.v alu.v tb.v
	PYTHONOPTIMIZE=${NOASSERT} vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

gtkwave_alu:
	gtkwave alu.vcd alu.gtkw

formal_alu:
	sby -f alu.sby
