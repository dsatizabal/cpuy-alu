`default_nettype none
`timescale 1ns/1ns

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test/test_*.py files
    input wire clk_tb,
    input wire rst_tb,
    input wire enable_tb,
    input wire [7:0] operation_tb,
    input wire [7:0] op1_tb,
    input wire [7:0] op2_tb,
	input wire cpu_carry_tb,
    output reg [7:0] result_l_tb,
    output reg [7:0] result_h_tb,
    output wire carry_tb,
    output wire zero_tb,
    output wire sign_tb
);

    // instantiate the DUT
    alu alu(
        .clk (clk_tb),
        .rst (rst_tb),
        .enable (enable_tb),
        .operation (operation_tb),
        .op1 (op1_tb),
        .op2 (op2_tb),
        .cpu_carry (cpu_carry_tb),
        .result_l (result_l_tb),
        .result_h (result_h_tb),
        .carry (carry_tb),
        .zero (zero_tb),
        .sign (sign_tb)
    );

endmodule
