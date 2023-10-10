
// Import the AuthService and axiosPrivate (mocked) for testing
import AuthService from '../auth.service';
import { axiosPrivate } from '../axios';
import jest from 'jest';
// Mock the axiosPrivate module to control its behavior during testing
jest.mock('./axios')

describe('AuthService', () => {
  // Mock the localStorage.setItem and localStorage.removeItem methods
  let setItemSpy;
  let removeItemSpy;

  beforeEach(() => {
    setItemSpy = jest.spyOn(Storage.prototype, 'setItem');
    removeItemSpy = jest.spyOn(Storage.prototype, 'removeItem');
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe('login', () => {
    it('should log in successfully', async () => {
      // Mock a successful login response
      axiosPrivate.post.mockResolvedValue({
        data: {
          isAuthenticated: true,
          username: 'testuser',
        },
      });

      const response = await AuthService.login('testuser', 'password123');

      expect(response.isAuthenticated).toBe(true);
      expect(setItemSpy).toHaveBeenCalledWith('user', expect.any(String));
    });

    it('should handle login error', async () => {
      // Mock a login error response
      axiosPrivate.post.mockRejectedValue({
        data: {
          error: 'Invalid credentials',
        },
      });

      try {
        await AuthService.login('invaliduser', 'wrongpassword');
      } catch (error) {
        expect(error.message).toBe('Invalid credentials');
      }
    });

    it('should handle connection error', async () => {
      // Mock a network connection error
      axiosPrivate.post.mockRejectedValue(new Error('Network error'));

      try {
        await AuthService.login('testuser', 'password123');
      } catch (error) {
        expect(error.message).toBe('Something went wrong. Please try again later.');
      }
    });
  });

  describe('logout', () => {
    it('should log out successfully', async () => {
      // Mock a successful logout response
      axiosPrivate.post.mockResolvedValue({});

      const response = await AuthService.logout();

      expect(response).toEqual({});
      expect(removeItemSpy).toHaveBeenCalledWith('user');
    });

    it('should handle connection error during logout', async () => {
      // Mock a network connection error during logout
      axiosPrivate.post.mockRejectedValue(new Error('Network error'));

      try {
        await AuthService.logout();
      } catch (error) {
        expect(error.message).toBe('Something went wrong. Please try again later.');
      }
    });
  });
});
