module dump();
	initial begin
		$dumpfile ("alu.vcd");
		$dumpvars (0, tb);
		#1;
	end
endmodule
