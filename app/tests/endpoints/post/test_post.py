from fastapi import status


class TestEndpointsPostClass:
	"""
	Post 엔드포인트에 대한 test case
	"""
	def setup(self):
		self.test_url = "/v1/post"
	
	def test_get_200_post(
			self,
			client,
	):
		response = client.get(
			url=self.test_url,
		)
		assert response.status_code is status.HTTP_200_OK
