import cocotb
from cocotb.triggers import ReadWrite, Timer


@cocotb.test()
async def dec_no_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 120
    dut.op2_tb.value = 0
    dut.operation_tb.value = 1 # Dec

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 119, f"Unexpected result L (after operation), expected 119 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def dec_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 1
    dut.op2_tb.value = 0
    dut.operation_tb.value = 1 # Dec

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def dec_sign(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 0
    dut.op2_tb.value = 0
    dut.operation_tb.value = 1 # Dec

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 1, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 1, f"Unexpected result L (after operation), expected 1 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def inc_no_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 120
    dut.op2_tb.value = 0
    dut.operation_tb.value = 2 # Inc

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 121, f"Unexpected result L (after operation), expected 121 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def inc_zero_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 255
    dut.op2_tb.value = 0
    dut.operation_tb.value = 2 # Inc

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 1, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def swap_no_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 158
    dut.op2_tb.value = 0
    dut.operation_tb.value = 10 # Swap

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 233, f"Unexpected result L (after operation), expected 233 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def swap_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 0
    dut.op2_tb.value = 0
    dut.operation_tb.value = 10 # Swap

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry";
    assert dut.sign_tb == 0, f"Unexpected sign";
    assert dut.zero_tb == 0, f"Unexpected zero";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 0, f"Unexpected carry (after operation)";
    assert dut.sign_tb == 0, f"Unexpected sign (after operation)";
    assert dut.zero_tb == 1, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 0, f"Unexpected result L (after operation), expected 0 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";
