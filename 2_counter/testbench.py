# Simple tests for an counter module
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

async def run_reset_routine(dut):
    for _ in range(2):
        await RisingEdge(dut.clk)
    dut.reset.value = 0

@cocotb.test()
async def basic_count(dut):
    # generate a clock
    cocotb.start_soon(Clock(dut.clk, 1, units="ns").start())

    # Reset DUT
    dut.reset.value = 1

    # reser the module, wait 2 rising edges until we release reset
    cocotb.start_soon(run_reset_routine(dut))


    # run for 50ns checking count on each rising edge
    for cnt in range(50):
        await RisingEdge(dut.clk)
        v_count = dut.count.value
        mod_cnt = cnt % 16
        #assert v_count.integer == mod_cnt, "counter result is incorrect: %s != %s" % (str(dut.count.value), mod_cnt)
        

