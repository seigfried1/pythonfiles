class Flight:
	def __init__(self, number, aircraft):
		if not number[:2].isalpha():
			raise ValueError("Noalpha")
		if not number[:2].isupper():
			raise ValueError("Nonumber")
		self._number = number
		self._aircraft = aircraft

		row, seats = self._aircraft.seating_plan()
		self._seating = [None] + [{letter:None for letter in seats} for _ in row]

	def number(self):
		return self._number
	def airline(self):
		return self._number[:2]
	def aircraft_model(self):
		return self._aircraft.model()

	def allocate_seat(self, seat, passenger):
		'''12F, 13C, etc'''
		rows, seat_letters = self._aircraft.seating_plan()
		seat_number_letter = seat[-1]
		if seat[-1] not in seat_letters:
			raise ValueError("Improper seat row")

		row_number = seat[:-1]
		try:
			int(row_number)
		except:
			raise ValueError("Improper seat number")
		
		if self._seating[int(row_number)][seat_number_letter] is None:
			self._seating[int(row_number)][seat_number_letter] = passenger
		else:
			raise ValueError("Seat Already Allocated")

	def relocate_passenger(self, seat, passenger):
		count = 0
		seat_row_number = 0
		dict_key = ''
		for i, dicts in enumerate(self._seating[1:]):
			for key in dicts:
				if passenger in [dicts[key]]:
					count += 1
					if count == 1:
						seat_row_number = i+1
						dict_key += key
		print(count)
		print(seat_row_number)
		if count == 0:
			raise ValueError("Passenger does not exist, relocation not possible")
		elif count == 1:
			print(self._seating[1:])		
			rows, seat_letters = self._aircraft.seating_plan()
			seat_number_letter = seat[-1]
			if seat_number_letter not in seat_letters:
				raise ValueError("Improper seat row")

			row_number = seat[:-1]
			try:
				int(row_number)
			except:
				raise ValueError("Improper seat number")

			self._seating[seat_row_number][dict_key] = None
			if self._seating[int(row_number)][seat_number_letter] is None:
				self._seating[int(row_number)][seat_number_letter] = passenger
			else:
				raise ValueError("Seat Already Allocated")


class Aircraft:
	def __init__(self, registration, model, num_rows, num_seats_per_row):
			self._registration = registration
			self._model = model
			self._num_rows = num_rows
			self._num_seats_per_row = num_seats_per_row

	def registration(self):
		return self._registration
	def model(self):
		return self._model
	def seating_plan(self):
		return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])

# a = Aircraft("G-EUPT", "airbus A210", 22, 6)
# print(a.registration())

# f = Flight("AA", a)
# print(f.aircraft_model())
