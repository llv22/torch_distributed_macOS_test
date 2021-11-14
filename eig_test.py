"""run.py:"""
#!/usr/bin/env python
import torch

a = torch.diag(torch.tensor([1, 2, 3], dtype=torch.double))
e, v = torch.eig(a)
print("e: {}, v: {}".format(e, v))
e, v = torch.eig(a, eigenvectors=True)
print("e: {}, v: {}".format(e, v))
