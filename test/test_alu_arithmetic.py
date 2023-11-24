import cocotb
from cocotb.triggers import ReadWrite, Timer


@cocotb.test()
async def add_no_carry_in_no_carry_out(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 2
    dut.op2_tb.value = 2
    dut.operation_tb.value = 136 # AddLW

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
    assert dut.result_l_tb == 4, f"Unexpected result L (after operation), expected 4 got {dut.result_l_tb}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def add_carry_in_no_carry_out(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 1

    dut.op1_tb.value = 2
    dut.op2_tb.value = 2
    dut.operation_tb.value = 136 # AddLW

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
    assert dut.result_l_tb == 5, f"Unexpected result L (after operation), expected 4 got {dut.result_l_tb}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def add_no_carry_in_carry_out(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 128
    dut.op2_tb.value = 129
    dut.operation_tb.value = 138 # AddLW

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry_tb";
    assert dut.sign_tb == 0, f"Unexpected sign_tb";
    assert dut.zero_tb == 0, f"Unexpected zero_tb";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 1, f"Expected carry (after operation)";
    assert dut.sign_tb == 0, f"Expected sign (after operation)";
    assert dut.zero_tb == 0, f"Expected zero (after operation)";
    assert dut.result_l_tb == 1, f"Unexpected result L (after operation), expected 1 got {dut.result_l_tb}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def add_carry_in_carry_out(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 1

    dut.op1_tb.value = 128
    dut.op2_tb.value = 129
    dut.operation_tb.value = 138 # AddLW

    dut.rst_tb.value = 1
    await ReadWrite()
    await Timer(10, units="ns");
    dut.rst_tb.value = 0

    assert dut.carry_tb == 0, f"Unexpected carry_tb";
    assert dut.sign_tb == 0, f"Unexpected sign_tb";
    assert dut.zero_tb == 0, f"Unexpected zero_tb";
    assert dut.result_l_tb == 0, f"Unexpected result L";
    assert dut.result_h_tb == 0, f"Unexpected result H";

    await ReadWrite()
    await Timer(10, units="ns");

    dut.enable_tb.value = 0
    assert dut.carry_tb == 1, f"Expected carry (after operation)";
    assert dut.sign_tb == 0, f"Expected sign (after operation)";
    assert dut.zero_tb == 0, f"Expected zero (after operation)";
    assert dut.result_l_tb == 2, f"Unexpected result L (after operation), expected 1 got {dut.result_l_tb}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def subb(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 100
    dut.op2_tb.value = 50
    dut.operation_tb.value = 140 # SubLW

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
    assert dut.result_l_tb == 50, f"Unexpected result L (after operation), expected 50 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def subb_with_sign(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 10
    dut.op2_tb.value = 50
    dut.operation_tb.value = 142 # SubMW

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
    assert dut.result_l_tb == 40, f"Unexpected result L (after operation), expected 40 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def subb_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 200
    dut.op2_tb.value = 200
    dut.operation_tb.value = 140 # SubLW

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
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def mult_single_byte(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 10
    dut.op2_tb.value = 10
    dut.operation_tb.value = 144 # MulLW

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
    assert dut.result_l_tb == 100, f"Unexpected result L (after operation), expected 100 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation)";

@cocotb.test()
async def mult_double_byte(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 100
    dut.op2_tb.value = 100
    dut.operation_tb.value = 146 # MulWM

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
    assert dut.result_l_tb == 16, f"Unexpected result L (after operation), expected 16 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 39, f"Unexpected result H (after operation), expected 39 got {dut.result_h_tb.value}";

@cocotb.test()
async def mult_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 100
    dut.op2_tb.value = 100
    dut.operation_tb.value = 146 # MulWM

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
    assert dut.result_l_tb == 16, f"Unexpected result L (after operation), expected 16 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 39, f"Unexpected result H (after operation), expected 39 got {dut.result_h_tb.value}";
