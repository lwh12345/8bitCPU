module Half_Adder(
	input	A,
	input	B,
	output	S,
	output	C
);

	// Xor(26, 14)
	xor xor_26x14(
		S,
		A,
		B
	);
	// And(26, 18)
	and and_26x18(
		C,
		A,
		B
	);

endmodule // Half_Adder
