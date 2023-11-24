import cocotb
from cocotb.triggers import ReadWrite, Timer


@cocotb.test()
async def rl_no_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 128
    dut.op2_tb.value = 0
    dut.operation_tb.value = 6 # RL

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
    assert dut.result_l_tb == 1, f"Unexpected result L (after operation), expected 1 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rl_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 0
    dut.op2_tb.value = 0
    dut.operation_tb.value = 6 # RL

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
async def rr_no_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 128
    dut.op2_tb.value = 0
    dut.operation_tb.value = 7 # RR

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
    assert dut.result_l_tb == 64, f"Unexpected result L (after operation), expected 64 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rr_zero(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 0
    dut.op2_tb.value = 0
    dut.operation_tb.value = 7 # RR

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
async def rlc_no_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 64
    dut.op2_tb.value = 0
    dut.operation_tb.value = 8 # RLC

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
    assert dut.result_l_tb == 128, f"Unexpected result L (after operation), expected 128 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rlc_cpu_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 1

    dut.op1_tb.value = 64
    dut.op2_tb.value = 0
    dut.operation_tb.value = 8 # RLC

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
    assert dut.result_l_tb == 129, f"Unexpected result L (after operation), expected 129 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rlc_carry_cpu_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 1

    dut.op1_tb.value = 192
    dut.op2_tb.value = 0
    dut.operation_tb.value = 8 # RLC

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
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 129, f"Unexpected result L (after operation), expected 129 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rlc_zero_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 128
    dut.op2_tb.value = 0
    dut.operation_tb.value = 8 # RLC

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
async def rrc_no_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 64
    dut.op2_tb.value = 0
    dut.operation_tb.value = 9 # RRC

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
    assert dut.result_l_tb == 32, f"Unexpected result L (after operation), expected 32 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rrc_cpu_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 1

    dut.op1_tb.value = 2
    dut.op2_tb.value = 0
    dut.operation_tb.value = 9 # RRC

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
    assert dut.result_l_tb == 129, f"Unexpected result L (after operation), expected 129 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rrc_carry_cpu_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 1

    dut.op1_tb.value = 7
    dut.op2_tb.value = 0
    dut.operation_tb.value = 9 # RRC

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
    assert dut.zero_tb == 0, f"Unexpected zero (after operation)";
    assert dut.result_l_tb == 131, f"Unexpected result L (after operation), expected 131 got {dut.result_l_tb.value}";
    assert dut.result_h_tb == 0, f"Unexpected result H (after operation), expected 0 got {dut.result_h_tb.value}";

@cocotb.test()
async def rrc_zero_carry(dut):
    dut.enable_tb.value = 1
    dut.cpu_carry_tb.value = 0

    dut.op1_tb.value = 1
    dut.op2_tb.value = 0
    dut.operation_tb.value = 9 # RRC

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
