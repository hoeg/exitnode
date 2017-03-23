from binaryninja import *

def highlightExitnodes(bv):
	for func in bv.functions:
		for block in func.basic_blocks:
			if len(block.outgoing_edges) == 0:
				block.set_user_highlight(HighlightStandardColor.RedHighlightColor)	

PluginCommand.register("Exitnodes", "Highlight exit nodes", highlightExitnodes)
