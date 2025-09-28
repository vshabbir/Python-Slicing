import slicer
message = "Hello"

print('Output from slicer: {} -- Output from python slicing: {}'.format(slicer.slice_string(message, -5, -1), message[-5:-1]))
print('Output from slicer: {} -- Output from python slicing: {}'.format(slicer.slice_string(message, -1, '', -1), message[-1::-1]))
print('Output from slicer: {} -- Output from python slicing: {}'.format(slicer.slice_string(message, '', '', -1), message[::-1]))
print('Output from slicer: {} -- Output from python slicing: {}'.format(slicer.slice_string(message, -1, -3, -1), message[-1:-3:-1]))
print('Output from slicer: {} -- Output from python slicing: {}'.format(slicer.slice_string(message, 1, '', 1), message[1::1]))
