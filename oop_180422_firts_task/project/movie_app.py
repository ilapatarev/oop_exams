from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
	def __init__(self):
		self.movies_collection=[]
		self.users_collection=[]

	def register_user(self, username, age):
		if username in [u.username for u in self.users_collection]:
			raise Exception("User already exists!")
		self.users_collection.append(User(username, age))
		return f"{username} registered successfully."

	def upload_movie(self,username, movie:Movie):
		if username not in [u.username for u in self.users_collection]:
			raise Exception("This user does not exist!")

		if movie.owner.username!=username:

			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		if movie.title in [m.title for m in self.movies_collection]:
			raise Exception("Movie already added to the collection!")

		self.movies_collection.append(movie)
		for u in self.users_collection:
			if u.username==username:
				u.movies_owned.append(movie)
		return f"{username} successfully added {movie.title} movie."

	def edit_movie(self, username, movie:Movie, **kwargs):

		if username not in [m.owner.username for m in self.movies_collection]:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		try:
			current_movie = next(filter(lambda m: m.title == movie.title, self.movies_collection))
		except StopIteration:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if kwargs:
			for item, value in kwargs.items():
				if item=='title':
					current_movie.title=kwargs[item]
				elif item=='year':
					current_movie.year=kwargs[item]
				elif item=='age_restriction':
					current_movie.age_restriction=kwargs[item]

			return f"{username} successfully edited {movie.title} movie."

	def delete_movie(self, username, movie:Movie):
		if username not in [m.owner.username for m in self.movies_collection]:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		try:
			current_movie = next(filter(lambda m: m.title == movie.title, self.movies_collection))
		except StopIteration:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		self.movies_collection.remove(current_movie)
		for u in self.users_collection:
			if u.username==username:
				u.movies_owned.remove(current_movie)
		return f"{username} successfully deleted {movie.title} movie."

	def like_movie(self, username, movie:Movie):
		if username not in [m.owner.username for m in self.movies_collection]:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		if movie.title in [u.movies_liked for u in self.users_collection]:
			raise Exception(f"{username} already liked the movie {movie.title}!")

		for m in self.movies_collection:
			if m.title==movie.title:
				m.likes+=1

		for u in self.users_collection:
			if u.username==username:
				u.movies_liked.append(movie)

		return f"{username} liked {movie.title} movie."

	def dislike_movie(self, username, movie:Movie):
		user=next(filter(lambda u: u.username == username, self.users_collection ))
		if movie not in user.movies_liked:
			raise Exception(f"{username} has not liked the movie {movie.title}!")
		for m in self.movies_collection:
			if m.title==movie.title:
				m.likes-=1
		user.movies_liked.remove(movie)
		return f"{username} disliked {movie.title} movie."

	def display_movies(self):
		if self.movies_collection:
			result=[]
			for y in sorted([n.year for n in self.movies_collection], reverse=True):
				for m in self.movies_collection:
					if m.year==y:
						result.append(m.details())
			return '\n'.join(result)
		else:
			return "No movies found."

	def __str__(self):
		result_users = []
		if self.users_collection:

			for u in self.users_collection:
				result_users.append(u.username)
		else:
			result_users.append("All users: No users.")

		result_movies=[]
		if self.movies_collection:
			for m in self.movies_collection:
				result_movies.append(m.title)

		else:
			result_movies.append("All movies: No movies.")

		return f"All users: {', '.join(result_users)}\n" \
		       f"All movies: {', '.join(result_movies)}"














