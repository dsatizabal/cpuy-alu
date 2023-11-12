import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles


@cocotb.test()
async def and_no_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 15
    dut.op2_tb.value = 8
    dut.operation_tb.value = 150 # And

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 8, f"Unexpected result L (after operation), expected 8 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def and_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 128
    dut.op2_tb.value = 8
    dut.operation_tb.value = 150 # And

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def or_no_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 133
    dut.op2_tb.value = 98
    dut.operation_tb.value = 152 # Or

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 231, f"Unexpected result L (after operation), expected 231 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def or_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 0
    dut.op2_tb.value = 0
    dut.operation_tb.value = 152 # Or

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def xor_no_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 133
    dut.op2_tb.value = 55
    dut.operation_tb.value = 154 # Xor

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 178, f"Unexpected result L (after operation), expected 178 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def xor_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 255
    dut.op2_tb.value = 255
    dut.operation_tb.value = 154 # Or

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def not_no_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 128
    dut.op2_tb.value = 0
    dut.operation_tb.value = 3 # Not

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 127, f"Unexpected result L (after operation), expected 127 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def not_zero(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 255
    dut.op2_tb.value = 0
    dut.operation_tb.value = 3 # Not

    dut.rst_tb.value = 1
    await ClockCycles(dut.clk_tb, 2)
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";
