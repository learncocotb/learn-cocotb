module count_up_tb();
wire [3:0] count;
reg clk,reset; 
count_up DUT(.clk(clk),.reset(reset),.count(count));
//iverilog -o count_up count_up.v count_up_tb.v
//vvp count_up
initial begin
    clk = 0; 
    forever #5 clk = ~clk; 
end

initial begin 
    $dumpfile("testbench.vcd");
    $dumpvars(0,DUT);
    reset = 0; 
    #5
    reset = 1; 
    #5
    reset = 0;  
    #15
    reset = 1; 
    #5
    reset = 0; 
    #200 $finish;
end

endmodule